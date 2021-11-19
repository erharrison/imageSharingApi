# imageSharingApi
## API Requirements
* ~~Images have a caption, limited to 100 chars.~~
* A user can follow/unfollow another user.
* Current user can like a post (image).
* List of images for the current user (most recent first, limited to users following).
* List of all posts (ordered by likes).
* List of all users (including information on the number of following and followers).
## Out of scope
* Sign up/registration - simple token management is fine.
* ~~Media/upload storage - assume this lives in a CDN and is accessed via a URL to the
image stored in the database.~~
* Production readiness - basic setup/SQLlite etc is fine.
* Note we are looking for an API and not a web application. You can test the API
using the command line (curl) or a tool such as Postman.

### Other Future Development
* Unit tests
