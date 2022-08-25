# from distutils.core import setup

# setup(name='remedies',
#       version='1.0.0',
#       py_modules=['remedies'],
#       install_requires=[
#         'flask',
#         'Flask-RESTful',
#       ],
#       author="ybbhfdf",
#       )


from setuptools import find_packages, setup

if __name__ == "__main__":
      setup(
          name='remedies',
          version='1.0.0',
          packages=find_packages(),
          include_package_data=True,
          zip_safe=False,
          install_requires=[
              'flask',
              'Flask-RESTful',
              'poetry'
          ],
      )
