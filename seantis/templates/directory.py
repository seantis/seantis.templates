import os

from templer.core.nested_namespace import NestedNamespace
from templer.core.vars import StringVar
from templer.core.structures import Structure

PROJECT_TITLE = StringVar(
    'project_title',
    title='Project Title',
    description=""
)

DIRECTORY_NAME = StringVar(
    'directory_name',
    title='Directory Name',
    description=""
)


class Basic(Structure):
    _structure_dir = 'structures/basic'


class Directory(NestedNamespace):
    _template_dir = 'templates/seantis_directory'
    summary = "A seantis.dir project"
    help = "Creates a basic seantis.dir project structure"
    category = 'Seantis'

    default_required_structures = ['basic']

    use_cheetah = True

    def pre(self, command, output_dir, vars):
        super(Directory, self).pre(command, output_dir, vars)
        vars['project_root'] = os.path.split(os.getcwd())[-1]

    def override_package_names_defaults(self, vars, expect_vars):
        super(Directory, self).override_package_names_defaults(
            vars, expect_vars
        )
        vars['expert_mode'] = 'all'

        assert 'seantis.dir' in vars['project'], """
            project must be named seantis.dir.* where * is your choice
        """
        structure = vars['project'].split('.')

        vars['namespace_package'] = structure[0]
        vars['namespace_package2'] = structure[1]
        vars['directory'] = vars['package'] = structure[2]
        vars['directory_name'] = structure[2].title()
        vars['zip_safe'] = False
        vars['project_title'] = ' '.join(structure).title()
