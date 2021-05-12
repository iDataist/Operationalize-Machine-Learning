# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import json
import logging
import os
import pickle
import numpy as np
import pandas as pd
import joblib

import azureml.automl.core
from azureml.automl.core.shared import logging_utilities, log_server
from azureml.telemetry import INSTRUMENTATION_KEY

from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType


input_sample = pd.DataFrame({"job_blue-collar": pd.Series([0], dtype="int64"), "job_entrepreneur": pd.Series([0], dtype="int64"), "job_housemaid": pd.Series([0], dtype="int64"), "job_management": pd.Series([0], dtype="int64"), "job_retired": pd.Series([0], dtype="int64"), "job_self-employed": pd.Series([0], dtype="int64"), "job_services": pd.Series([0], dtype="int64"), "job_student": pd.Series([0], dtype="int64"), "job_technician": pd.Series([0], dtype="int64"), "job_unemployed": pd.Series([0], dtype="int64"), "job_unknown": pd.Series([0], dtype="int64"), "marital_married": pd.Series([0], dtype="int64"), "marital_single": pd.Series([0], dtype="int64"), "marital_unknown": pd.Series([0], dtype="int64"), "education_basic_6y": pd.Series([0], dtype="int64"), "education_basic_9y": pd.Series([0], dtype="int64"), "education_high_school": pd.Series([0], dtype="int64"), "education_illiterate": pd.Series([0], dtype="int64"), "education_professional_course": pd.Series([0], dtype="int64"), "education_university_degree": pd.Series([0], dtype="int64"), "education_unknown": pd.Series([0], dtype="int64"), "default_unknown": pd.Series([0], dtype="int64"), "default_yes": pd.Series([0], dtype="int64"), "housing_unknown": pd.Series([0], dtype="int64"), "housing_yes": pd.Series([0], dtype="int64"), "loan_unknown": pd.Series([0], dtype="int64"), "loan_yes": pd.Series([0], dtype="int64"), "contact_telephone": pd.Series([0], dtype="int64"), "month_aug": pd.Series([0], dtype="int64"), "month_dec": pd.Series([0], dtype="int64"), "month_jul": pd.Series([0], dtype="int64"), "month_jun": pd.Series([0], dtype="int64"), "month_mar": pd.Series([0], dtype="int64"), "month_may": pd.Series([0], dtype="int64"), "month_nov": pd.Series([0], dtype="int64"), "month_oct": pd.Series([0], dtype="int64"), "month_sep": pd.Series([0], dtype="int64"), "day_of_week_mon": pd.Series([0], dtype="int64"), "day_of_week_thu": pd.Series([0], dtype="int64"), "day_of_week_tue": pd.Series([0], dtype="int64"), "day_of_week_wed": pd.Series([0], dtype="int64"), "poutcome_nonexistent": pd.Series([0], dtype="int64"), "poutcome_success": pd.Series([0], dtype="int64"), "age": pd.Series([0.0], dtype="float64"), "duration": pd.Series([0.0], dtype="float64"), "campaign": pd.Series([0.0], dtype="float64"), "pdays": pd.Series([0.0], dtype="float64"), "previous": pd.Series([0.0], dtype="float64"), "emp_var_rate": pd.Series([0.0], dtype="float64"), "cons_price_idx": pd.Series([0.0], dtype="float64"), "cons_conf_idx": pd.Series([0.0], dtype="float64"), "euribor3m": pd.Series([0.0], dtype="float64"), "nr_employed": pd.Series([0.0], dtype="float64")})
output_sample = np.array([0])
try:
    log_server.enable_telemetry(INSTRUMENTATION_KEY)
    log_server.set_verbosity('INFO')
    logger = logging.getLogger('azureml.automl.core.scoring_script')
except:
    pass


def init():
    global model
    # This name is model.id of model that we want to deploy deserialize the model file back
    # into a sklearn model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')
    path = os.path.normpath(model_path)
    path_split = path.split(os.sep)
    log_server.update_custom_dimensions({'model_name': path_split[-3], 'model_version': path_split[-2]})
    try:
        logger.info("Loading model from path.")
        model = joblib.load(model_path)
        logger.info("Loading successful.")
    except Exception as e:
        logging_utilities.log_traceback(e, logger)
        raise


@input_schema('data', PandasParameterType(input_sample))
@output_schema(NumpyParameterType(output_sample))
def run(data):
    try:
        result = model.predict(data)
        return json.dumps({"result": result.tolist()})
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})
