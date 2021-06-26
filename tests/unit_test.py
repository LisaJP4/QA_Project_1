from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Types, Reports
from application import routes

class TestApp(TestCase):
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

class TestRead(TestApp):
    def test_reports_get(self):
        response = self.client.get(url_for('readreports'))
        self.assertEqual(response.status_code, 200)

    def test_reports_get(self):
        response = self.client.get(url_for('readreports'))
        self.assertIn(b'Logged Issues', response.data)

    def test_policy_get(self):
        response = self.client.get(url_for('policies'))
        self.assertEqual(response.status_code, 200)

class TestAss(TestApp):
    def test_add_report(self):
        response = self.client.post(
            url_for('newreport'),
            data = dict(product_section="Gardening Equipment", report_type="Damage", description="Test description", resolution="Nothing yet", complete="Y"),
            follow_redirects=True
        )
        self.assertIn(b'Gardening Equipment',response.data)
        self.assertIn(b'Damage', response.data)
        self.assertIn(b'Test description', response.data)
        self.assertIn(b'Nothing yet', response.data)
        self.assertIn(b'Y', response.data)

 

