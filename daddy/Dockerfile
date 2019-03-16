FROM ruby:2.6.2-alpine

RUN apk update && apk upgrade && apk add --update alpine-sdk
ADD . /code
WORKDIR /code
RUN bundle install && bundle clean
CMD ["ruby", "app.rb"]
