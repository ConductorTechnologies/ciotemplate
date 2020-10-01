### Version:0.2.11 -- 01 Oct 2020

* Package environment now allows exclusive override. [481851b]
* Allow relative paths that start with letter, colon - it could happen. [241fc68]

### Version:0.2.10 -- 08 Sep 2020

* Gpath allow colons in paths. [9c19d3a]
 
### Version:0.2.9 -- 06 Sep 2020

* Sequence consumers must use factory. [01a7dd7]

### Version:0.2.8 -- 03 Sep 2020

* Tidy and remove dependency on future. [0c2f72c]

### Version:0.2.7 -- 28 Aug 2020

* Adds cycle_progressions chunk strategy for improved scout frame distribution. [9b42288]
* Remove yaml config (#8)
* Remove config file references
* Adds jwt domain validation for credentials file so token is renewed when switching Google projects. 
* Api_url defaults to same domain as auth_url

### Version:0.2.6 -- 18 Aug 2020

* Adds jwt domain validation for creds file. [0042b2b]
* Remove config file references. [451896b]

### Version:0.2.5 -- 11 Aug 2020

* Production release

### Version:0.2.4 -- 11 Aug 2020

* Removed redshift package ids hack. [8d11367]

### Version:0.2.3 -- 10 Aug 2020

* Adds remove_missing files method to Gpath. [3b96796]
* Adds validators base class. [c91ffc9] [b074cce]

### Version:0.2.2 -- 08 Aug 2020

* Temp workarounds for missing plugin-host links in packages
* Remove "shared" request.session object. (#293)
* Update httpbatchworker docstring (#291)
* File api refactor multipart and tcp connection pooling (#290)
* Multipart updates to workers
* Add make_preapred_request for s3 calls to remove transfer-encoding header being added. update descriptions and v2 endpoints. Add content-length for s3 calls. don't return response object on s3 calls which can cause a build up of memory due to jobworker, return headers or none.
* Add metric_store increments for aws presigned and multipart, cannot use chunked reader since generator does not have len function.
* Use httpbatchworker response to avoid additional os.stat calls. [7c76c46]

### Version:0.2.1 -- 01 Aug 2020

* Minor

### Version:0.2.0 -- 01 Aug 2020

* Use explicit entry point script. [dfd9da3]
* The coredata singleton that holds instance_types, projects, and software must now be initialized with software product. This is to avoid having to specify the product on every call to data(). [db0fcb0]
* Expander context made public to indicate to other objects that they may retrieve the context. [a457aa1]

### Version:0.1.15 -- 27 Jul 2020

* Made post install script runnable. [8dce89f]

### Version:0.1.14 -- 27 Jul 2020

* Simplified post install script - no longer interactive. [6bba8af]

### Version:0.1.13 -- 26 Jul 2020

* Refactored post install setup script. [3fbba5e]


### Version:0.1.12 -- 25 Jul 2020

* Setup can accept cmdline args for non-wizard mode. [f195b7d]
* Adds safe mode to expander. [95f6cfd]

### Version:0.1.11 -- 22 Jul 2020

* Adds Setup wizard to make installation easier. [a06d610]

### Version:0.1.10 -- 21 Jul 2020

* Use cio to differentiate from conductor. [3f49451]
* Projects and instance types sorted for fixtures. [4a0f833]

### Version:0.1.9 -- 10 Jul 2020

* Implement data singletons here and remove from conductor-maya. [d31aeaa]

### Version:0.1.8 -- 06 Jul 2020

* Repair some path list issues found while adding remove method. [7368cc2]

### Version:0.1.7 -- 04 Jul 2020

* Adds a remove method to pathlist. [5712d2c]
* Wip configure script. [e7f6ea9]

### Version:0.1.6 -- 29 Jun 2020

* Fix bad path to conductor cmd. [5be12af]
* Packages: Remove tree property and make _tree -> tree. [1e6ae34]

### Version:0.1.5 -- 22 Jun 2020

* Remove src. [a366047]
* Newline in requirements. [a4cd9d3]
* Missing member. [b2bfb6d]
* Fix tests. [c9498c9]
* Imports ciocore. [916651e]
* Flatten. [c88afae]
* Flatter hierarchy. [6906e23]
* Slug means local slug. [0db16e0]
* Init declare namespace. [84d16b3]
* Use underscore name. [1aae967]
* Correct namespace config. [22a09f3]


### Version:0.1.4 -- 14 Jun 2020

* Ignore build dir. [8080df5]
