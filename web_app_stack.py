from aws_cdk import (
    aws_s3 as s3,
    aws_apigateway as apigateway,
    aws_lambda as lambda_,
    core
)

class WebAppStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # S3 Bucket for frontend
        bucket = s3.Bucket(self, "FrontendBucket", versioned=True)

        # Lambda backend
        backend = lambda_.Function(self, "BackendFunction",
                                    runtime=lambda_.Runtime.PYTHON_3_9,
                                    handler="app.lambda_handler",
                                    code=lambda_.Code.from_asset("../backend"))

        # API Gateway
        api = apigateway.LambdaRestApi(self, "APIEndpoint",
                                       handler=backend)

        # Outputs
        core.CfnOutput(self, "BucketName", value=bucket.bucket_name)
        core.CfnOutput(self, "APIEndpoint", value=api.url)
