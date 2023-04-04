#!/usr/bin/env bash

function main() {
  docker build -t book_parser:latest .
  docker run --name book_parser-$RANDOM book_parser:latest | tee output.txt
}

main
