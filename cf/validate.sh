## References
# https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html
# https://docs.aws.amazon.com/cli/latest/reference/cloudformation/validate-template.html
# https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-validate-template.html
# https://aws.amazon.com/premiumsupport/knowledge-center/cloudformation-template-validation/

$ aws cloudformation validate-template --template-url file://example.json

# or 

$ aws cloudformation validate-template --template-body file://example.json