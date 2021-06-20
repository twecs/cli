import setuptools


packages = setuptools.find_namespace_packages(
    include=[
        'twecs.*',
    ],
)

setuptools.setup(
    entry_points={
        'console_scripts': [
            'twecs = twecs.cli:entry_point',
        ],
    },
    extras_require={
        'notifier-email': [
            'twecs.notifiers.email >= 0.1 , < 1.0',
        ],
        'notifier-todoist': [
            'twecs.notifiers.todoist >= 0.1 , < 1.0',
        ],
    },
    install_requires=[
        'pyxdg == 0.27',
        'PyYAML == 5.4.1',
        'twecs_wise >= 0.1 , < 1.0',
    ],
    name='twecs.cli',
    packages=packages,
    python_requires='>= 3.8',
    version='0.1',
    zip_safe=False, # due to namespace package
)
