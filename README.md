# Gene-Expression Programming on OpenAI atari environments


Gene-Expression Programming based technique applied on [OpenAI gym atari](https://github.com/openai/gym) environmets. 

This repository contains the implementation of an evolutionary algorithm to train agents so they can improve their behavior on atari environments. 

* Offspring is generated only by mutation.
* Mutation is implemented as a matrix multiplication. 



#### Running code 

First install dependencies: 

``` bash 
pip install -r requirements.txt
```

To execute code run 

``` bash
python main.py --env=<ENV_NAME> --step=<STEPS_TO_RUN>
```

For more information about the parameters run 
``` bash
python main.py --help
```


#### Example 
``` bash 
python main.py --steps=50000000 --env=MsPacman-ram-v4
```


#### References: 

1. [Gene Expression Programming](https://arxiv.org/pdf/cs/0102027.pdf)