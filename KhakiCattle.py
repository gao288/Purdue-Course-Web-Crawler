
import http.client
import sys
import time
import urllib.request as urllib2
# from email.mime.text import MIMEText
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

   #Initializing lists
   lsStartTags = list()
   lsEndTags = list()
   lsStartEndTags = list()
   lsComments = list()

   #HTML Parser Methods
   def handle_starttag(self, startTag, attrs):
       print("Start tag:", startTag)
       for attr in attrs:
           print("     attr:", attr)

   def handle_endtag(self, endTag):
       self.lsEndTags.append(endTag)

   def handle_startendtag(self,startendTag, attrs):
       self.lsStartEndTags.append(startendTag)

   def handle_comment(self,data):
       self.lsComments.append(data)


def REST_api(crn):
    parser = MyHTMLParser()
    to_get = "/prod/bwckschd.p_disp_detail_sched?term_in=201920&crn_in=" + crn
    html_page = urllib2.openurl("https://selfservice.mypurdue.purdue.edu/prod/bwckschd.p_disp_detail_sched?term_in=201930&crn_in=12112")
    # Feeding the content
    parser.feed(str(html_page.read()))

# def parse_html(body):
#     parser = MyHTMLParser()
#     parser.feed(body)


def main():
    REST_api("15365")
    #parse_html(body)


if __name__ == "__main__": main()
