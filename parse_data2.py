from pm4py.objects.log.importer.xes import factory as xes_import_factory

path_log = "C:\personal projects\ISMFieldproject\data\Hospital_log.xes"
path_billing = "C:\personal projects\ISMFieldproject\data\Hospital Billing - Event Log.xes.gz"
path_sepsis = "C:\personal projects\ISMFieldproject\data\Sepsis Cases - Event Log.xes.gz"

# %% we read in the event docs from xes

hospital_log = xes_import_factory.apply(path_log)
hospital_billing = xes_import_factory.apply(path_billing)
sepsis_cases = xes_import_factory.apply(path_sepsis)


# %% we transform the documents into csv files

from pm4py.objects.log.exporter.csv import factory as csv_exporter

csv_exporter.export(hospital_log, "hospital_log.csv")
csv_exporter.export(hospital_billing, "hospital_billing.csv")
csv_exporter.export(sepsis_cases, "sepsis_cases.csv")

