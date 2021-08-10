# Introduction to Amazon SageMaker
## Topics we will be covered in this chapter.
1. Auto managing services by SageMaker
    * Infrastructrue
    * Auto Scaling
    * All ML packages or Dependencies
    * Deployment and so on
2. We will focuse in this chapter
    * Solve pain points faced by ML practioners
    * SageMaker Capabilities
        * Demonstrating the strengths 
    * Setup SageMaker / local machine configeruation.
        * SageMaker **notebook instance**
        * Setting up Amazon **SageMaker Studio**

~~ Code examples included in the book are available on GitHub at https://github.
com/PacktPublishing/Learn-Amazon-SageMaker. You will need to install a Git
client to access them (https://git-scm.com/). ~~        
----
# Technical requirements
1. [AWS Account](https://aws.amazon.com/getting-started/)
2. [Free Tier](https://aws.amazon.com/free/)
3. Required Installations
    * [AWS CLI](https://aws.amazon.com/cli/)
    * Python 3.x (use anaconda distributors)
        * we will need (Jupyter, pandas, numpy, and more).

## SageMaker Capabilities
* Launched at AWS re:Invent 2017
* [SageMaker Features complete List](https://aws.amazon.com/about-aws/whats-new/machine-learning)
* SageMaker Application Programming Interfaces (**APIs**), and the Software Development Kits (**SDKs**)
* **The main capabilities of Amazon SageMaker**:
    Amazon SageMaker is the ability to build, train, optimize, and deploy
    models on fully managed infrastructure, and at any scale
    * ## Building
    1. SageMaker provides you with two development environments
        * Notebook Instance: EC2, Jupyter, Anaconda and so on.
    2. SageMaker Studio:
        * Full-fledged integrated development environment
    3. 17 Built-in Alogrithms: ML, DL Optimized to run efficiently on AWS. NO ML code to write!
    4. Open source frameworks (Tensorflow, Pytorch, Apache, MXNet, scikit-learn and more)
    5. Your own code running in your own container: Custom ** Python, R, C++, Java and so on**.
    6. [Pre-trained Models ](https://aws.amazon.com/marketplace/solutions/machine-learning).
    7. <span style="color:red">Amazon SageMaker Autopilot</span> uses AutoML to automatically build, train,and optimize models without the need to write a single line of ML code.
    8. Data Prepairing (data pre-processing)
        * Amazon SageMaker Ground Truth
        * Amazon SageMaker Processing: Run data processing and model evaluation batch
        jobs, using either scikit-learn or Spark
    * ## Training
    1. Managed Storage: S3, Amazon EFS or Amazon FSx for Luster depending on your performance requirements
    2. Managed spot training: Using EC2 spot instance for training in order to reduce costs by up to 80%
    3. Distributed Training: Large-Scale training jobs on a cluster of managed instances.
    4. Pip mode: streams infinitely large datasets in S3, Saving the need to copy data around.
    5. <span style="color: red">Automatic model tuning</span>: runs hyperparameters optimization in order ot deliver high-accuracy model more quickly.
    6. Amazon SageMaker Experiments: 
        * tracks
        * Organize
        * compare all sageMaker jobs
    7. Debugger:
        * Capture internal state during training
        * Inspects observe how the model learns
        * Detects unwanted conditions that hurt accuracy.
    * ## Deploying<br>
    Just as with training, Amazon SageMaker takes care of all your deployment infrastructure,
    and brings a slew of additional features:
    1. Real-time endpoints: HTTPS API
        * Server prediction from your model
        * auto-scaling
    2. Batch-Transform: 
        * predict data in batch
    3. CloudWatch
        * Real-time Infra-structure monitering 
    4. Model Monitor:<br>This captures data sent to an endpoint, and
    compares it with a baseline to identify and alert on data quality issues (missing
    features, data drift, and more)
    5. Amazon SageMaker Neo:
        * compile model for specific hardware (edge,sensor)
        * embeded platform and deploys an optimized version using lightweight runtime.
    6. **Amazon Elastic Inference**: This add fractional GPU acceleration to CPU-based instances for best cost ratio for your prediction inftrastructure.
    ----
## The Amazon SageMaker API

Amazon SageMaker is driven by APIs that are implemented in the language SDKs supported by AWS (https://aws.amazon.com/tools/).
   * Python SDK
   * aka the 'SageMaker SDK'
#### The AWS language SDKs
   * Language SDK's implement service-specific API for all AWS S3, EC2 and so on.
   * [SageMaker API](https://docs.aws.amazon.com/sagemaker/latest/dg/api-and-sdk-reference.html)
   * [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html). SageMaker APIs Available in boto3. 
        * This API low level and verbose
        * create_training_job() has a lot of JSON parameters.
        * We don't need to manage Infrastructure as a code with **CloudFormation** this tool use your deveOps team.
        * We use SageMaker SDK instead of **CloudFormation**
   * SageMaker SDK
        * SageMaker SDK is a python SDK specific. [click of details](https://github.com/aws/sagemaker-pythonsdk)
        * [documentation](https://sagemaker.readthedocs.io/en/stable/)
        * <span style="color:red">The code examples in this book are based on the first release of the SageMaker SDK v2</span>
        * Extremely easy and comfortable to fire up a training job (One line of code) and to deploye a model (one line of code). Infrastructure concerns are abstracted away.
        ```
        # Configure the training job
        my_estimator = TensorFlow(
            'my_script.py',
            role=my_sageMaker_role,
            instance_type='ml.p3.2xlarge',
            instance_count=1,
            framework_version='2.1.0')
        # Train the model
        my_estimator.fit('s3://my_bucket/my_training_data/')

        # Deploy the model to an HTTPS endpoint
        my_predictor = my_estimator.deploy(
            initial_instance_count=1,
            instance_type='ml.c5.2xlarge')
        ```


---
# Demonstrating the strengths of Amazon SageMaker
## Alice's and Bob's Problems
   * Solving Alice's problems
      * she is PHD and data Scientist, She is expert in Math and Statistics
      * She focus on data, advancing her research and publishing papers.
      * She don't know much about IT infrastructure, and she honestly doesn't care all for these topics.
      * She work on her desktop workstation
         * She manage her Desktop
         * Install all packages and software
         * When something goes wrong, she wastes precious hours fixing it.
      * She also have remote servers with powerful multi-GPU, connected to petabyte of network-attached storage.
         * Teh team leads meet and try to prioritize projects and workload.
      * ## Let's see how SageMaker and cloud computing can help Alice.
         * Inexpensive SageMaker notebook instance in a minute.
         * Run code own demand on CPU, GPU's and cluster with managing infrastructure.
         * Automatic model tuning feature in SageMaker
         * Deploying models with cople on lines
         * Keeping track of her expenses with AWS console.
## Solving Bob's problems
   * Bob's history
      * He is DevOps engineer,
      * In charge of a large training cluster share by a team of data scientists
         * Setup Auto scaling
         * Capacity planning is still needed to find the right amout of EC2 instances and to optimize the cost using the right mix of reserved.
         * Bob tries to autmatically reduce capacity at night and on weekends when cluster is less busy.
         * Applied **CI/CD**, After validating model
            * dockerize/containers
            * He just hopes that no one will ask him to do PyTorch and Apache MXNet too.
      * ## Let's see how Bob could use SageMaker to improve his ML workflows.            


