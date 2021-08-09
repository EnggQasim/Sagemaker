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



    



