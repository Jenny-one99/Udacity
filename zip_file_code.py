mkdir my-sourcecode-function

cd my-sourcecode-function

pip install --target ./package sagemaker

cd package
zip -r ../my-deployment-package.zip .

cd ..
zip -g my-deployment-package.zip lambda_function.py

