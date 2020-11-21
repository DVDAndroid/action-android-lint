# GitHub Action: Run Android Lint with reviewdog

This action runs [Android Lint](https://developer.android.com/studio/write/lint) with
[reviewdog](https://github.com/reviewdog/reviewdog).

## Inputs

#### `github_token`

**Required**. Must be in form of `github_token: ${{ secrets.github_token }}`.

#### `lint_xml_file`

**Required**. Location of Android Lint XML file.

#### `level`

Optional. Report level for reviewdog [`info`,`warning`,`error`].
It's same as `-level` flag of reviewdog.
The default is `error`.

#### `reporter`

Optional. Reporter of reviewdog command [`github-check`, `github-pr-check`,`github-pr-review`].
The default is `github-check`.

#### `reviewdog_flags`

Optional. Additional flags to be passed to reviewdog cli.
The default is ``.

## Example usage

[Example repo](https://github.com/DVDAndroid/action-android-lint-example)

```yml
name: CI

on: [push, pull_request]

jobs:
  build:
    name: CI Build
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@master

      - name: Setup JDK 8
        uses: actions/setup-java@master
        with:
          java-version: 8

      - name: Grant execute permission for gradlew
        run: chmod +x gradlew

      - name: Run Gradle build
        run: ./gradlew build

      - name: Run Android Lint
        uses: dvdandroid/action-android-lint@master
        with:
          github_token: ${{ secrets.TOKEN_GITHUB }}
          lint_xml_file: app/build/reports/lint-results.xml
```

Note: `lint-results.xml` must be available; you need to `gradlew build` your application first

### Credits

I used [ScaCap/action-ktlint](https://github.com/ScaCap/action-ktlint) as a template