class GCPPrivateOfferMessage:
    def __init__(self, tenantid, queuemessage):
        self.tenantid = tenantid
        self.queuemessage = queuemessage

    class GCPProductAndPlan:
        def __init__(self, offertitle):
            self.offertitle = offertitle

    class GCPPrivateOfferModel:
            def __init__(self, projectid, dealreferenceid, gcpproductandplan):
                self.projectid = projectid
                self.dealreferenceid = dealreferenceid
                self.gcpproductandplan = gcpproductandplan


