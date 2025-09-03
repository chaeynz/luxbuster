FROM alpine:3.22.1 AS builder

RUN apk update && \
    apk add go git

RUN go install github.com/OJ/gobuster/v3@latest


FROM alpine:3.22.1 AS final

COPY --from=builder /root/go/bin/gobuster /usr/bin/gobuster

RUN adduser -D appuser

USER appuser

ENTRYPOINT [ "gobuster" ]
