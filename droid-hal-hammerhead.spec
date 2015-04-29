# These and other macros are documented in dhd/droid-hal-device.inc

%define device hammerhead
%define vendor lge

%define vendor_pretty LG
%define device_pretty Nexus 5

%define installable_zip 1

# Entries migrated from the old rpm/droid-hal-hammerhead.spec
%define enable_kernel_update 1

%include rpm/dhd/droid-hal-device.inc
