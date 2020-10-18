# provision-gcp-qwiklabs

### While doing [Qwiklabs](https://www.qwiklabs.com/), you are given a temporary GCP account to perform all the tasks. with each lab, you need to login and accept all T&C's, etc. which is annoying and time-consuming. here's a python script to automate all that so you can focus more on labs :)

<br>

## To set-up follow these steps:

<br>

requires [Python v3](https://www.python.org/downloads/) to run.

1. Clone this repo.

```sh
$ git clone https://github.com/parshnt/provision-gcp-qwiklabs.git
```

2. Check your chrome version by visiting `chrome://settings/help` and download the appropriate version of ChromeDriver from [here](https://chromedriver.chromium.org/downloads). Place the chromedriver executable inside this project's folder.


3. Navigate inside the folder and Install the requirements.

```sh
$ cd provision-gcp-qwiklabs
$ pip install -r requirements.txt
```

4. Run `python main.py` and enter the details :)
