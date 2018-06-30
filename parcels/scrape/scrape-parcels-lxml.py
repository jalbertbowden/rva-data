import lxml.html as LH
import requests
import json

# id attribute value uppnXMLControl has all desired data
#XPATH_HTML_CONTENT = '//div[@id="uppnXMLControl"]'
#htmlContent = parser.xpath(XPATH_HTML_CONTENT)

"""
url options:
http://eservices.ci.richmond.va.us/applications/propertysearch/Print.aspx?pin=N0001591006

Print Entire Reports
http://eservices.ci.richmond.va.us/applications/propertysearch/Print.aspx?pin=N0001591006&PrintType=Report

print this page
http://eservices.ci.richmond.va.us/applications/propertysearch/Print.aspx?pin=E0001096014&PrintType=Screen&ActiveTabIndex=0&SubTabIndex=
"""


baseURL = "http://eservices.ci.richmond.va.us/applications/propertysearch/Detail.aspx?pin=E0001096014"

tree = LH.parse(baseURL)


"""
parcel property header
"""

# parcel property header labels
propAddressHeaderLabels = []
propertyAddressHeaders = tree.xpath('//div[@id="uppnXMLControl"]/div/div[@class="smallHeading"]/b/text()')
for propertyAddressHeader in propertyAddressHeaders:
	propertyAddressHeader = propertyAddressHeader.lstrip()
	propAddressHeaderLabels.append(propertyAddressHeader.rstrip())

# parcel property header values
propAddressHeaderDetails = []
propertyAddressHeaderDetails = tree.xpath('//div[@id="uppnXMLControl"]/div/div[@class="smallHeading"]/text()')
for propertyAddressHeaderDetail in propertyAddressHeaderDetails:
	#print propertyAddressHeaderDetail
	propertyAddressHeaderDetail = propertyAddressHeaderDetail.lstrip()
	propAddressHeaderDetails.append(propertyAddressHeaderDetail.rstrip())
#print propAddressHeaderDetails

propAddressHeaderOutput = []

propAddressHeaderOutputFirstRow = "URL", baseURL
#print propAddressHeaderOutputFirstRow
propAddressHeaderOutput.append(propAddressHeaderOutputFirstRow)

for headerLabel,headerValue in zip(propAddressHeaderLabels,propAddressHeaderDetails):
	headerRow = headerLabel, headerValue
	propAddressHeaderOutput.append(headerRow)
	#print headerLabel, headerValue

#print propAddressHeaderOutput

"""
parcel property section headers
"""

# parcel property section headers values
tabHeadings = tree.xpath('//fieldset[@class="detailSet"]/legend/text()')

tabHeaders = []
for tabHeader in tabHeadings:
	tabHeaders.append(tabHeader)
#print "fieldset legend headers"
#print tabHeaders

# labels span[@class="columnLabel")
# values span[@class="fieldValue")

res_dict = {"parcel": propAddressHeaderOutput + tabHeaders }
to_json = json.dumps(res_dict)


with open('test-output.json', 'w') as outfile:
	json.dump(to_json, outfile)
