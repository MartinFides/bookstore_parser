#!/usr/bin/env bash

function main() {
  docker-compose build
  docker-compose run --rm bookstore_parser
}

main
