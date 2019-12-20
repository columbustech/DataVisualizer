from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import os, sys, json
import requests
import pdb
from myapp.models import Document
from myapp.forms import DocumentForm
from utils.utils import *
import numpy as np
import matplotlib.pyplot as plt

REDIRECT_URI = os.environ["CDRIVE_URL"] + "app/" + os.environ["COLUMBUS_USERNAME"] + "/string-prepper/"
APP_ID = os.environ["COLUMBUS_CLIENT_ID"]
APP_SECRET = os.environ["COLUMBUS_CLIENT_SECRET"]
TOKEN_URL = os.environ["AUTHENTICATION_URL"] + "o/token/"
AUTH_URL = os.environ["AUTHENTICATION_URL"] + "o/authorize/" + "?response_type=code" + "&client_id=" + os.environ["COLUMBUS_CLIENT_ID"] + "&redirect_uri=" + REDIRECT_URI + "&state=1234xyz"
CDRIVE_URL = os.environ["CDRIVE_API_URL"]
CDRIVE_UI_URL = os.environ["CDRIVE_URL"]
CLIENT_TOKEN_KEY = "procleaner_token"
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
CDRIVE_FILES_DIR = os.path.join(PROJECT_DIR, "cdrive_files")
# Create your views here.
def sample(request):
    """
    View for rendering the sample tuples of the uploaded file.
    This view does the following:
        1. Read the upload type.
        2. Save the uploaded file locally.
        3. Set session parameters to reference the file subsequently.
        4. Read and return a sample of tuples.
    Arguments:
        request: The request object.
    Returns an HttpResponse object.
    """
    upload_type = ""
    cdrive_file_path = request.POST.get('cdriveFile')
    

	data = np.genfromtxt("data.csv", delimiter=",")
	plt.imshow(data, cmap='hot', interpolation='nearest')
	plt.show()
    return render(request, 'sample.html', {'sample_tuples': sample_tuples})
