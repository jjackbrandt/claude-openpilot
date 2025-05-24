# Tesla Pre-AP Model S Support - Installation Guide

## ⚠️ Current Status: IN DEVELOPMENT

This repository is currently being debugged for installation compatibility. The Tesla implementation is complete but there are boot issues being resolved.

## 🔧 Known Issue

Currently experiencing a boot loop where the installer shows "installing jjackbrandt" at 0% progress, shows tinkla splash, then returns to setup.

This is likely due to:
1. Missing submodule dependencies in the official 0.9.8 structure  
2. Incompatible car interface loading
3. AGNOS compatibility issues

## 🛠️ Current Fix In Progress

We are working on resolving this by:
1. Identifying the minimal required changes to official 0.9.8
2. Ensuring Tesla functionality without breaking the base system
3. Testing installation compatibility with comma installer

## 📞 Alternative Installation

If you need Tesla pre-AP support immediately, consider using the original tinkla fork:
- https://github.com/tinkla/openpilot

## 🔄 Updates

This README will be updated once the installation issues are resolved.

---

**Work in progress - do not use for installation yet!**