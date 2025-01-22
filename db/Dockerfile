FROM golang:alpine AS builder

LABEL name="goose"
RUN go install github.com/pressly/goose/v3/cmd/goose@latest

FROM alpine:latest
WORKDIR /

COPY --from=builder /go/bin/goose /go/bin/goose

RUN ls

ENTRYPOINT ["/go/bin/goose", "-dir=/migrations", "postgres"]