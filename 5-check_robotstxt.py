#!/usr/bin/env python
'''
Check robots.txt file and save a version every time it changes.

@author:    Jean-Christophe Chouinard. 
@role:      Sr. SEO Specialist at SEEK.com.au
@website:   jcchouinard.com
@LinkedIn:  linkedin.com/in/jeanchristophechouinard/ 
@Twitter:   twitter.com/@ChouinardJC

What it does:
Fetch Robots.txt. 
Read each line in the file. 
Save the file with the date. 
If a robots.txt file exists from a previous extraction, check if the file has changed. 
If it hase changed, save a new version and send an Alert. 
This way, you don’t need to save a file every day, only when it changes.
'''

from datetime import datetime
import easygui
import os
import time

from functions import create_project, fetch_page, get_date, get_domain_directory

robotstxt = 'http://127.0.0.1:5000/robots.txt'
# robotstxt = 'https://www.jcchouinard.com/robots.txt'

def main(url,filename='robots.txt'):
    '''
    Combine all functions
    '''
    path = os.getcwd()
    site = get_domain_directory(robotstxt)
    output = path + '/output/' + site + '/'
    create_project(output)
    r = fetch_page(url)
    output_files = get_robots_files(output)
    compare_robots(output, output_files,r)

def get_robots_files(directory):
    '''
    List robots.txt file in output folder
    '''
    output_files = os.listdir(directory)
    output_files.sort()
    return output_files

def get_robotstxt_name(output_files):
    '''
    Get last saved robots.txt file.
    '''
    robots_txt = 'robots.txt'
    files = []
    for filename in output_files:
        if robots_txt in filename:
            files.append(filename)
    return files[-1]

def read_robotstxt(filename):
    '''
    Read robots.txt
    '''
    if os.path.isfile(filename):
        with open(filename,'r') as f:
            txt = f.read()
    return txt

def write_robotstxt(file, output, filename='robots.txt'):
    '''
    Write robots.txt to file using date as identifier.
    '''
    filename = get_date() + '-' + filename
    filename = output + filename
    with open(filename,'w') as f:
        f.write(file)

def compare_robots(output,output_files,r):
    '''
    Compare previous robots to actual robots.
    If different. Save File.
    '''
    new_robotstxt = r.text.replace('\r', '')

    if output_files:
        robots_filename = get_robotstxt_name(output_files) 
        filename = output + robots_filename
        last_robotstxt = read_robotstxt(filename)
        last_robotstxt = last_robotstxt.replace('\r', '')
        if new_robotstxt != last_robotstxt:
            print('Robots.txt was modified')
            write_robotstxt(new_robotstxt, output)
            easygui.msgbox(f'The Robots.txt was changed for {filename}', title="simple gui")
            # For simplicity. I would send an email or a slack notification instead.
        else:
            print('No Change to Robots.txt')
    else:
        print('No Existing Robots.txt. Saving one.')
        write_robotstxt(r.text, output)

if __name__ == '__main__':
    main(robotstxt)


# filename ='/Users/jean.christophe/Documents/Github/PVT-SEO-PROJECTS/Python/Selenium/ranksense-selenium/output/2020-10-02:13:3314-robots.txt'
# with open(filename, 'r') as f:
#     print(''.join(f.readlines()))
