from flask import url_for
from flask_testing import TestCase, LiveServerTestCase
from application import app, db
from application.models import Types, Reports
from application import routes


class TestApp(LiveServerTestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='sdkfjvn',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

        
    def setUp(self):
        db.create_all()
        samplereport1 = Reports(product_section="Outdoor Plants", description="Patricia [employee] slipped on spilled water leaking out of the outdoor plants onto the patio", complete="N", report_type="Injury")
        samplereport2 = Types(type_id="Damage", severity="Medium", role_responsibility="Employee", fixed_in_days=7, policies="In case of damage, either accidental or deliberate, employees should hastily clear the area to ensure customer safety")
        db.session.add(samplereport1)
        db.session.add(samplereport2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestReports(TestApp):
    def submit_empty(self):
        self.driver.find_element_by_xpath(//*[@id="complete"]).send_keys("")
        self.driver.find_element_by_xpath(//*[@id="submit"]).click()

    def test_