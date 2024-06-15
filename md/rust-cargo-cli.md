---
id: 2024-04-16_rust-cargo-cli
aliases: 
tags:
  - code
date: 2024-05-16
type: note
links:
  - "[[python]]"
  - "[[code]]"
  - "[[rust]]"
  - "[[cli]]"
---

# rust cargo cli


rustc --version
cargo new PROJECTNAME

## Faster Linking 
With lld

```toml
[target.x86_64-unknown-linux-gnu]
rustflags = ["-C", "linker=clang", "-C", "link-arg=-fuse-ld=lld"]

[target.x86_64-pc-windows-msvc]
rustflags = ["-C", "link-arg=-fuse-ld=lld"]

[target.x86_64-pc-windows-gnu]
rustflags = ["-C", "link-arg=-fuse-ld=lld"]

[target.x86_64-apple-darwin]
rustflags = ["-C", "link-arg=-fuse-ld=lld"]

[target.aarch64-apple-darwin]
rustflags = ["-C", "link-arg=-fuse-ld=/opt/homebrew/opt/llvm/bin/ld64.lld"]
```

### cargo-watch

cargo install cargo-watch
cargp watch -x check

### Testing

cargo test

### Code coverage

cargo install cargo-tarpaulin
cargo cargo-tarpaulin --ignore-tests

### Linting

rustup component add clippy
cargo clippy
cargo clippy -- -D warnings

### Formatting

rustup component add rustfmt
cargo fmt
cargo fmt -- --check

### Auditing

cargo install cargo-audit
cargo audit
