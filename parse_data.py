import gzip
import sys
import _io
import io
from opyenxes.data_in import XesXmlParser, XesXmlGZIPParser

xes = XesXmlParser.XesXmlParser()
xes_gzip = XesXmlGZIPParser.XesXmlGZIPParser()


path_log = "C:\personal projects\ISMFieldproject\data\Hospital_log.xes"
path_billing = "C:\personal projects\ISMFieldproject\data\Hospital Billing - Event Log.xes.gz"
path_sepsis = "C:\personal projects\ISMFieldproject\data\Sepsis Cases - Event Log.xes.gz"

# %% Testing if I can parse the files

if xes.can_parse(path_log):
    print("it is possible to parse the normal xes file")
else:
    print("cannot handle")

if xes_gzip.can_parse(path_log):
    print("normal file with special one")
else:
    print("gzipparser cannot parse the normal xes")

if xes_gzip.can_parse(path_billing):
    print("the gzip can be opened haleluja!!")
else:
    print("bwuuuuup")

# %% we need to configure some extensions in order to parse the files

"""
Unknown extension: http://www.xes-standard.org/meta_time.xesext
Unknown extension: http://www.xes-standard.org/meta_life.xesext
Unknown extension: http://www.xes-standard.org/meta_org.xesext
Unknown extension: http://www.xes-standard.org/meta_concept.xesext
Unknown extension: http://www.xes-standard.org/meta_3TU.xesext
Unknown extension: http://www.xes-standard.org/meta_general.xesext
"""

from opyenxes.extension.XExtension import XExtension
from opyenxes.extension.XExtensionManager import XExtensionManager
from urllib.parse import urlparse

manager = XExtensionManager()

manager.register(XExtension("MetaData_Time", "meta_time", urlparse("http://www.xes-standard.org/meta_time.xesext")))
manager.register(XExtension("MetaData_LifeCycle", "meta_life", urlparse("http://www.xes-standard.org/meta_life.xesext")))
manager.register(XExtension(name="MetaData_Organization", prefix="meta_org", uri=urlparse("http://www.xes-standard.org/meta_org.xesext")))
manager.register(XExtension(name="MetaData_Concept", prefix="meta_concept", uri=urlparse("http://www.xes-standard.org/meta_concept.xesext")))
manager.register(XExtension(name="MetaData_3TU", prefix="meta_3TU", uri=urlparse("http://www.xes-standard.org/meta_3TU.xesext")))
manager.register(XExtension(name="MetaData_General", prefix="meta_general", uri=urlparse("http://www.xes-standard.org/meta_general.xesext")))

# %% let´s parse the files

try:
    log_file = xes.parse(open(path_log))
    print("success for hospital_log")
except:
    print("we couldn´t parse hospital logs")
try:
    billing_file = xes_gzip.parse(open(path_billing))
    print("success for hospital billing")
except:
    print("we couldn´t parse billing logs")
try:
    sepsis_file = xes_gzip.parse(open(path_sepsis))
    print("success for sepsis cases")
except:
    print("we couldn´t parse scepsis")


# %% let´s get some info about our logs

from opyenxes.info.XLogInfo import XLogInfo

test = XLogInfo(log_file[0], default_classifier=None, classifiers=None)




# %% let´s get the attributes

from opyenxes.info.XAttributeInfo import XAttributeInfo

test = XAttributeInfo().get_attributes()
