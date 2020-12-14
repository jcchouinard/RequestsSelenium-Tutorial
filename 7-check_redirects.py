#!/usr/bin/env python
'''
Make a Redirection Report

@author:    Jean-Christophe Chouinard. 
@role:      Sr. SEO Specialist at SEEK.com.au
@website:   jcchouinard.com
@LinkedIn:  linkedin.com/in/jeanchristophechouinard/ 
@Twitter:   twitter.com/@ChouinardJC

What it does:
Crawl a list of URLs.
Count the number of redirects.
Check if it has a redirect or a canonical loop
Report on errors.
'''
import os
import pandas as pd
from urllib.parse import urljoin

from functions import create_project, fetch_page, get_domain_name, get_canonical_from_html

urls = [
    'http://127.0.0.1:5000/page',
    'http://127.0.0.1:5000/redirect-301',
    'http://127.0.0.1:5000/multiple_r/0',
    'http://127.0.0.1:5000/redirect-loop',
    'http://127.0.0.1:5000/canonical-loop',
    'http://127.0.0.1:5000/timeout'
    ]

def check_redirects(url_list):
    '''
    Loop through each URL.
    Fetch the page
    Counts the number of redirects
    Check Canonical
    Return data or errors
    '''
    df = pd.DataFrame()
    for i in range(len(url_list)): 
        url = url_list[i]
        domain = get_domain_name(url)

        r = fetch_page(url) 

        df.loc[i,'start_url'] = url

        if type(r) == str: # If there is an error
            df.loc[i,'error_type'] = r
            df.loc[i,'destination_url'] = 'Error'
            if df.loc[i,'error_type'] == 'TooManyRedirects':
                df.loc[i,'loop'] = 'Yes'
                df.loc[i,'num_redirects'] = 30.0
        else:    
            df.loc[i,'destination_url'] = r.url
            df.loc[i,'destination_status'] = r.status_code
            df.loc[i,'num_redirects'] = len(r.history)
            df.loc[i,'loop'] = 'No'
            if r.status_code == 200:
                canonical = get_canonical_from_html(r)
                df.loc[i,'canonical'] = canonical[1]
                absolute_canonical = urljoin(domain, canonical[1])
                if absolute_canonical == url:
                    df.loc[i,'loop'] = 'Yes'
        df.to_csv(filename)
    return df

def highlight_errors(x):
    '''
    highlight the maximum in a Series yellow.
    '''
    if x['destination_status'] != 200 or x['loop'] == 'Yes':
        return ['color: #d65f5f'] * 7
    else:
        return ['color: #5fba7d'] * 7 

if __name__ == '__main__':
    path = os.getcwd()
    directory = path + '/output/'
    create_project(directory)
    filename = directory + 'redirect_report.csv'
    df = check_redirects(urls)
    df.style.apply(highlight_errors, axis=1)
## For those who would like to add the list of redirects to the df
# for j in range(1,len(r.history)):
#     status = r.history[j].status_code
#     url = r.history[j].url.replace(domain,'')
#     df.loc[i,f'redirect_{j}_url'] = url
#     df.loc[i,f'redirect_{j}_stats'] = status


