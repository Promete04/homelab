# My Homelab Repository

Welcome to my homelab repository! This project serves as a central hub for all the resources, configurations, and documentation related to my homelab setup. It's a personal journey into learning, experimenting, and improving my knowledge of networking, server management, virtualization, and automation.

## Introduction

This homelab is a hands-on exploration of IT infrastructure, designed to help me learn and experiment with cutting-edge tools, best practices, and technologies. From building virtual environments to automating processes, my homelab is a playground for innovation.
> [!WARNING]  
> This repository is part of an experimentation project. As such, some configurations, setups, or approaches documented here may not follow best practices, may contain errors, or may require improvement. Feedback is always welcomed!

The primary goals of this project include:
- Deepening my understanding of systems administration, networking, and virtualization.
- Creating a scalable and efficient setup for personal and educational use.
- Experimenting with new software and tools.

## Hardware Used

Here's a list of the hardware powering my homelab:
- **Primary Server**: Dell Optiplex 9020
  - CPU: Intel Core i5-4590x4
  - RAM: 16GB DDR3
  - Storage: 500GB SATA SSD + 500GB HDD + ~~External drive (mounted internally — failed, unusable)~~
    > Attempted to salvage a previously damaged drive. Recovery of undamaged sectors was unsuccessful; drive is no longer in use.
<img src="https://github.com/Promete04/homelab/blob/main/pictures/Setup/ex_internal_drive.jpeg" width=300><img src="https://github.com/Promete04/homelab/blob/main/pictures/Setup/ex_internal_drive1.jpeg" width=300> 

- **High Performance Server**: Asus TUF Dash F15 2022 (FX517ZM)
  - CPU: 12th Gen Intel Core i7-12650H
  - GPU: NVIDIA RTX 3060 6GB
  - RAM: 16GB DDR5
  - Storage: 500GB NVMe SSD + 1TB NVMe SSD
- **NAS**: HP ProLiant MicroServer G7 N54L
  - CPU: AMD Turion II Neo N54L
  - RAM: 16GB DDR3
  - Storage: 250GB SATA SSD + 4TB HDD
- **Networking Gear**: Generic 5-port gigabit switch
- **UPS**: Woxter UPS 800 VA

## Software Used

The homelab runs a mix of open-source and commercial software. Key components include:
- **Hypervisor**: Proxmox *(2-node cluster)*
  - **Node: Entrypoint** (Dell Optiplex 9020) — Containers:
    - 100 tailscale LXC *(primary VPN tunnel)*
    - 103 tailscale LXC *(backup — failover in case the primary goes down)*
    - 104 web-check LXC
    - 106 shelfmark LXC
    - 107 drawio LXC
    - 108 joplin-server LXC
    - 110 openwebui LXC
    - 113 bentopdf LXC
    - 115 n8n LXC
    - 116 alpine-adguard LXC
  - **Node: Entrypoint** — VMs:
    - 112 haos (Home Assistant OS)
  - **Node: asus** (Asus TUF Dash F15 2022) — Containers:
    - 101 cloudfared LXC
    - 102 jellyfin LXC *(GPU-accelerated transcoding via RTX 3060)*
    - 105 booklore LXC
    - 109 ollama LXC *(GPU-accelerated — runs 7B and 9B(not so good) parameter models via RTX 3060)*
    - 114 discopanel LXC
  - **Node: asus** — VMs:
    - 111 docker
- **NAS**: TrueNAS Scale
  - **Containers**:
    - immich

## Pictures
A picture speaks a thousand words! Below are snapshots of my setup: 

<img src="https://github.com/Promete04/homelab/blob/main/pictures/Setup/shark.jpeg" width=300 height=300> 

- **Homelab diagram**:  
     <img src="https://github.com/Promete04/homelab/blob/main/pictures/Diagrams/homelab.drawio.png" >
     > The diagram was heavily influenced by [TechGeek01's Homelab Stuff](https://homelab.techgeek01.com).
- **Setup**:  
     <img src="https://github.com/Promete04/homelab/blob/main/pictures/Setup/setup1.jpeg">
     <img src="https://github.com/Promete04/homelab/blob/main/pictures/Setup/setup2.jpeg" width=300>
     <img src="https://github.com/Promete04/homelab/blob/main/pictures/Setup/array.jpg" width=300>
     > The HP server was designed to house 3.5" drives and included the railing for it. Due to only having 2.5" drives, I "MacGyvered" a solution with packaging material I had laying around.  
- **Dashboard Previews**:  
   <img src="https://github.com/Promete04/homelab/blob/main/pictures/Dashboards/dashboard.png" >  
   <img src="https://github.com/Promete04/homelab/blob/main/pictures/Dashboards/drives.png" >

## Repository Contents

This repository will contain:
- **Configuration Files**: `.conf`, `.yaml`, `.json`, `.ini` files for various tools.
- **Scripts**: Any Bash, Python, or PowerShell scripts for automation or maintenance.
- **Documentation**: Markdown files explaining setups, troubleshooting guides, and best practices.
- **Network Diagrams**: Visuals created with tools like draw.io.
- **Logs and Reports**: Sanitized logs or performance benchmarking results.

---
