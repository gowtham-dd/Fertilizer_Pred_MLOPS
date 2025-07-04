# from src.Fertilizer_Pred.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
# from src.Fertilizer_Pred.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
# from src.Fertilizer_Pred.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
# from src.Fertilizer_Pred.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline
# import dagshub
# dagshub.init(repo_owner='gowtham-dd', repo_name='winepred-MLFLOW', mlflow=True)
from src.Fertilizer_Pred.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from Fertilizer_Pred import logger

STAGE_NAME="Data Ingestion stage"


try:
    logger.info(f">>>> Stage {STAGE_NAME} started")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e

