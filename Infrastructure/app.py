from aws_cdk import App
from stacks.web_app_stack import WebAppStack

app = App()
WebAppStack(app, "WebAppStack")
app.synth()
