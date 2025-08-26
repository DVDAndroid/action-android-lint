FROM alpine:3.11

RUN apk --no-cache --update add git python3 \
    && rm -rf /var/cache/apk/*

RUN wget -O - -q https://raw.githubusercontent.com/reviewdog/reviewdog/fd59714416d6d9a1c0692d872e38e7f8448df4fc/install.sh| sh -s

COPY entrypoint.sh /entrypoint.sh
COPY converter.py /usr/local/bin/converter.py

ENTRYPOINT ["/entrypoint.sh"]
