# Copyright (C) 2014-2015 Jurriaan Bremer.
# This file is part of VMCloak - http://www.vmcloak.org/.
# See the file 'docs/LICENSE.txt' for copying permission.


VBOX_CONFIG = {
    'VBoxInternal/Devices/pcbios/0/Config': dict(

        # http://blog.prowling.nu/2012/08/modifying-virtualbox-settings-for.html
        DmiBIOSFirmwareMajor=('bios', 'firmware_major'),
        DmiBIOSFirmwareMinor=('bios', 'firmware_minor'),
        DmiBIOSReleaseDate=('bios', 'release_date'),
        DmiBIOSReleaseMajor=('bios', 'release_major'),
        DmiBIOSReleaseMinor=('bios', 'release_minor'),
        DmiBIOSVendor=('bios', 'vendor'),
        DmiBIOSVersion=('bios', 'version'),

        DmiChassisAssetTag=('chassis', 'asset'),
        DmiChassisSerial=('chassis', 'serial'),
        DmiChassisVendor=('chassis', 'vendor'),
        DmiChassisVersion=('chassis', 'version'),
        DmiChassisType=('chassis', 'type'),

        # http://blog.prowling.nu/2012/10/modifying-virtualbox-settings-for.html
        DmiBoardVendor=('board', 'vendor'),
        DmiBoardProduct=('board', 'product'),
        DmiBoardVersion=('board', 'version'),
        DmiBoardSerial=('board', 'serial'),
        DmiBoardAssetTag=('board', 'asset'),
        DmiBoardLocInChass=('board', 'location'),
        DmiBoardBoardType=('board', 'type'),

        DmiSystemVendor=('system', 'vendor'),
        DmiSystemProduct=('system', 'product'),
        DmiSystemVersion=('system', 'version'),
        DmiSystemSerial=('system', 'serial'),
        DmiSystemSKU=('system', 'sku'),
        DmiSystemFamily=('system', 'family'),
        DmiSystemUuid=('system', 'uuid'),

        DmiOEMVBoxVer=('oem_vbox', 'ver'),
        DmiOEMVBoxRev=('oem_vbox', 'rev'),

        BiosRom=('bios', 'bios_rom_path'),
        LanBootRom=('bios', 'lan_boot_rom_path'),
    ),
    'VBoxInternal/Devices/piix3ide/0/Config': {
        'Port0': dict(

            # http://downloads.cuckoosandbox.org/slides/blackhat.pdf, Page 82
            # https://forums.virtualbox.org/viewtopic.php?f=1&t=48718
            # ATAPIProductId='',
            # ATAPIRevision='',
            # ATAPIVendorId='',
        ),
        'PrimaryMaster': dict(

            # http://blog.prowling.nu/2012/08/modifying-virtualbox-settings-for.html
            SerialNumber=('primary_master', 'serial'),
            FirmwareRevision=('primary_master', 'revision'),
            ModelNumber=('primary_master', 'model'),
        ),
        'SecondaryMaster': dict(

            # http://blog.prowling.nu/2012/08/modifying-virtualbox-settings-for.html
            SerialNumber=('secondary_master', 'serial'),
            FirmwareRevision=('secondary_master', 'revision'),
            ModelNumber=('secondary_master', 'model'),
            ATAPIVendorId=('secondary_master', 'atapi_vendor'),
            ATAPIProductId=('secondary_master', 'atapi_product'),
            ATAPIRevision=('secondary_master', 'atapi_revision'),
        ),
    },
    'VBoxInternal/Devices/acpi/0/Config': dict(
        AcpiOemId=('acpi', 'oem'),
        DsdtFilePath=('acpi', 'dsdt_path'),
        SsdtFilePath=('acpi', 'ssdt_path'),
    ),
    'VBoxInternal/Devices/vga/0/Config': dict(
        BiosRom=('vga', 'bios_rom_path'),
    ),
}
