from django.shortcuts import render
import joblib
import json,os
import numpy as np
import pandas as pd
import psycopg2

# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    model = joblib.load('../models/models.joblib')
    return render(request, 'index.html')