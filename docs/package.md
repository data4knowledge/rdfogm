# Building a Package

## Tools

Install the following
```
pip install wheel    
pip install twine     
```

## Building

Build as follows
```
python setup.py sdist bdist_wheel       
twine check dist/*    
twine upload --repository-url https://test.pypi.org/legacy/ dist/*     
````

## Example Session

```
(env) python/rdfogm % python setup.py sdist bdist_wheel  
running sdist
running egg_info
writing rdfogm.egg-info/PKG-INFO
writing dependency_links to rdfogm.egg-info/dependency_links.txt
writing requirements to rdfogm.egg-info/requires.txt
writing top-level names to rdfogm.egg-info/top_level.txt
reading manifest file 'rdfogm.egg-info/SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'rdfogm.egg-info/SOURCES.txt'
running check
warning: Check: missing required meta-data: url

creating rdfogm-0.0.2
creating rdfogm-0.0.2/rdfogm
creating rdfogm-0.0.2/rdfogm.egg-info
copying files to rdfogm-0.0.2...
copying LICENSE -> rdfogm-0.0.2
copying README.md -> rdfogm-0.0.2
copying setup.cfg -> rdfogm-0.0.2
copying setup.py -> rdfogm-0.0.2
copying rdfogm/__init__.py -> rdfogm-0.0.2/rdfogm
copying rdfogm/base_property.py -> rdfogm-0.0.2/rdfogm
copying rdfogm/connection.py -> rdfogm-0.0.2/rdfogm
copying rdfogm/data_property.py -> rdfogm-0.0.2/rdfogm
copying rdfogm/object_property.py -> rdfogm-0.0.2/rdfogm
copying rdfogm/property_literal.py -> rdfogm-0.0.2/rdfogm
copying rdfogm/property_uri.py -> rdfogm-0.0.2/rdfogm
copying rdfogm/property_value.py -> rdfogm-0.0.2/rdfogm
copying rdfogm/rdf_type_property.py -> rdfogm-0.0.2/rdfogm
copying rdfogm/settings.py -> rdfogm-0.0.2/rdfogm
copying rdfogm.egg-info/PKG-INFO -> rdfogm-0.0.2/rdfogm.egg-info
copying rdfogm.egg-info/SOURCES.txt -> rdfogm-0.0.2/rdfogm.egg-info
copying rdfogm.egg-info/dependency_links.txt -> rdfogm-0.0.2/rdfogm.egg-info
copying rdfogm.egg-info/requires.txt -> rdfogm-0.0.2/rdfogm.egg-info
copying rdfogm.egg-info/top_level.txt -> rdfogm-0.0.2/rdfogm.egg-info
Writing rdfogm-0.0.2/setup.cfg
creating dist
Creating tar archive
removing 'rdfogm-0.0.2' (and everything under it)
running bdist_wheel
running build
running build_py
creating build
creating build/lib
creating build/lib/rdfogm
copying rdfogm/base_property.py -> build/lib/rdfogm
copying rdfogm/object_property.py -> build/lib/rdfogm
copying rdfogm/property_value.py -> build/lib/rdfogm
copying rdfogm/__init__.py -> build/lib/rdfogm
copying rdfogm/property_uri.py -> build/lib/rdfogm
copying rdfogm/connection.py -> build/lib/rdfogm
copying rdfogm/data_property.py -> build/lib/rdfogm
copying rdfogm/settings.py -> build/lib/rdfogm
copying rdfogm/rdf_type_property.py -> build/lib/rdfogm
copying rdfogm/property_literal.py -> build/lib/rdfogm
installing to build/bdist.macosx-10.9-universal2/wheel
running install
running install_lib
creating build/bdist.macosx-10.9-universal2
creating build/bdist.macosx-10.9-universal2/wheel
creating build/bdist.macosx-10.9-universal2/wheel/rdfogm
copying build/lib/rdfogm/base_property.py -> build/bdist.macosx-10.9-universal2/wheel/rdfogm
copying build/lib/rdfogm/object_property.py -> build/bdist.macosx-10.9-universal2/wheel/rdfogm
copying build/lib/rdfogm/property_value.py -> build/bdist.macosx-10.9-universal2/wheel/rdfogm
copying build/lib/rdfogm/__init__.py -> build/bdist.macosx-10.9-universal2/wheel/rdfogm
copying build/lib/rdfogm/property_uri.py -> build/bdist.macosx-10.9-universal2/wheel/rdfogm
copying build/lib/rdfogm/connection.py -> build/bdist.macosx-10.9-universal2/wheel/rdfogm
copying build/lib/rdfogm/data_property.py -> build/bdist.macosx-10.9-universal2/wheel/rdfogm
copying build/lib/rdfogm/settings.py -> build/bdist.macosx-10.9-universal2/wheel/rdfogm
copying build/lib/rdfogm/rdf_type_property.py -> build/bdist.macosx-10.9-universal2/wheel/rdfogm
copying build/lib/rdfogm/property_literal.py -> build/bdist.macosx-10.9-universal2/wheel/rdfogm
running install_egg_info
Copying rdfogm.egg-info to build/bdist.macosx-10.9-universal2/wheel/rdfogm-0.0.2-py3.10.egg-info
running install_scripts
adding license file "LICENSE" (matched pattern "LICEN[CS]E*")
creating build/bdist.macosx-10.9-universal2/wheel/rdfogm-0.0.2.dist-info/WHEEL
creating 'dist/rdfogm-0.0.2-py3-none-any.whl' and adding 'build/bdist.macosx-10.9-universal2/wheel' to it
adding 'rdfogm/__init__.py'
adding 'rdfogm/base_property.py'
adding 'rdfogm/connection.py'
adding 'rdfogm/data_property.py'
adding 'rdfogm/object_property.py'
adding 'rdfogm/property_literal.py'
adding 'rdfogm/property_uri.py'
adding 'rdfogm/property_value.py'
adding 'rdfogm/rdf_type_property.py'
adding 'rdfogm/settings.py'
adding 'rdfogm-0.0.2.dist-info/LICENSE'
adding 'rdfogm-0.0.2.dist-info/METADATA'
adding 'rdfogm-0.0.2.dist-info/WHEEL'
adding 'rdfogm-0.0.2.dist-info/top_level.txt'
adding 'rdfogm-0.0.2.dist-info/RECORD'
removing build/bdist.macosx-10.9-universal2/wheel
(env) python/rdfogm % twine check dist/*  
Checking dist/rdfogm-0.0.2-py3-none-any.whl: PASSED, with warnings
  warning: `long_description_content_type` missing. defaulting to `text/x-rst`.
Checking dist/rdfogm-0.0.2.tar.gz: PASSED, with warnings
  warning: `long_description_content_type` missing. defaulting to `text/x-rst`.
(env) python/rdfogm % twine upload --repository-url https://test.pypi.org/legacy/ dist/*     

Uploading distributions to https://test.pypi.org/legacy/
Enter your username: daveih   
Enter your password: 
Uploading rdfogm-0.0.2-py3-none-any.whl
100%|█████████████████████████████████████████████████████████████████████████████████████████████| 14.5k/14.5k [00:01<00:00, 9.14kB/s]
Uploading rdfogm-0.0.2.tar.gz
100%|█████████████████████████████████████████████████████████████████████████████████████████████| 12.4k/12.4k [00:01<00:00, 11.3kB/s]

View at:
https://test.pypi.org/project/rdfogm/0.0.2/
(env) python/rdfogm % 
```