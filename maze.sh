#!/bin/bash

for counter in $(seq 1 10000); do c=(╱ ╲);printf ${c[RANDOM%2]} ; done

