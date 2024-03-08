# my-library

This is an almost empty Python package with Sphinx documentation.

The goal is to create a project that publishes different versions of the documentation together. Like [Read the Docs](https://about.readthedocs.com/) does.

When using Read the Docs, I don't have to worry about creating a directory structure to store each version of the documentation, they do that. Also they provide the hosting, and some other valuable features. This project tries to accomplish something similar using resources under your control.

## Lifecycle of my-library

Usually the lifecycle of a library consist of fixing bugs, and developing enhancements and features. In order for the library to have an impact in other projects it often has documentation.

While the code of the library evolves the documentation follows along:

* Bug fixes sometimes are only documented in the ChangeLog when a patch release is produced. The patch release triggers the build of the docs, even if they only list the bugs fixed during the release. Say we have passed from v2.1.5 to v2.1.6. We want the docs of v2.1.6 to overwrite the docs of v2.1.5 in the URL https://example.com/my-library/2.1/.
* Enhancements and new features normally require new documentation or rewritting some parts of it. A new minor release, say from v2.1.6 to v2.2.0 offers new features or enhancements worth mentioning. For reasons beyond our knowledge, people using v2.1 might need to stick to that version. And therefore the docs for v2.2 will be different from the docs for v2.1.
* When new features and enhancements force us to break backwards compatibility, we make a major release, maybe from v2.2 to v3.0. The changes are usually explained in the docs. Projects using our library will not simply switch to a new major release without carefully evaluating the consequences.

It is clear that having docs for different versions is important to avoid leaving people behind. While our library progresses, projects using it will benefit from having access to previous versions' documentation.

The docs are generated with every release:

* With patch changes the docs are rewritten. We decided not keep available docs for v2.1.5 and v2.1.6. We just keep the latest docs produced under the version number  v2.1.
* With minor releases there is a new documentation site produced. If previous version was v2.1 and new version is v2.2. They both will be available as:
  - https://my-library.docs.org/2.1
  - https://my-library.docs.org/2.2
* With major releases there is also a new documentation site available. From v2.x to v3.0, the new docs will be available as:
  - https://my-library.docs.org/3.0

## Release tools

This particular example repository uses:

* GitHub Actions associated with release tags to trigger the creation of the docs for the new release. Any other CI/CD tool would work as well for the same purpose.
* AWS S3, to place the generated docs in a specific directory structure to support multiple versions. Any other cloud provider, or your own on-premises resources would follow the same logic.
* Sphinx as the documentation static site generator. But any other would make it too.

## The site layout

The same web server will be serving all the versions:

* **v1.0** will be serve in `https://my-library.docs.org/1.0/`
* **v1.1** will be serve in `https://my-library.docs.org/1.1/`, and so on.

Sphinx will produce the content served from each of those URLs. When GitHub Actions run the publishing of the docs for version **X.Y**, Sphinx will produce the static site that is placed under the path `/X.Y/`, which will match the directory `/X.Y/` in the S3 bucket.

The script running in GitHub Actions extracts the `X.Y` from the release in course. If the release is 1.1.4, the `X.Y` is `1.1`, and the docs will be publish under that directory.
