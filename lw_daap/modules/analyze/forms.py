from invenio.utils.forms import InvenioBaseForm
from wtforms import RadioField, SelectField, StringField, validators

from .utils import get_requirements

class LaunchForm(InvenioBaseForm):
    name = StringField(
        label = 'Instance Name',
        description= 'Required. A name that helps to identify your instance',
        validators=[validators.DataRequired(),
                    validators.length(
                        max=50,
                        message=("The identifier must be less "
                                 "than 50 characters long.")),
                   ],
    )
    
    flavor = SelectField(
        label = 'Flavor',
        description = 'Required. Size of the VM to start',
    )

    image = SelectField(
        label = 'Operating System',
        description = 'Required. Operating System to use',
    )

    app_env = SelectField(
        label = 'Application environment',
        description = 'Required. Some info?',
    )

    def _build_choices(self, reqs, req_type):
        return [(k, v['title']) for k, v in reqs.get(req_type, {}).items()]

    def fill_fields_choices(self):
        reqs = get_requirements()
        self.flavor.choices = self._build_choices(reqs, 'flavors')
        self.image.choices = self._build_choices(reqs, 'images')
        self.app_env.choices = self._build_choices(reqs, 'app_envs')

    