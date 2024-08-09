#!/bin/bash
zig build-exe hello-zig.zig
rm *.o
cp hello-zig ../src/hello/