class Preference:

    APPOINTMENT_REASON_INSPECTION = 'inspection'
    APPOINTMENT_REASON_BASICTUNEUP = 'basic tuneup'
    APPOINTMENT_REASON_ADVANCEDTUNEUP = 'advanced tuneup'
    APPOINTMENT_REASON_FLATFIX = 'flat-fix'
    APPOINTMENT_REASON_ASSEMBLY = 'bike assembly'
    APPOINTMENT_REASON_BIKEPACK = 'bike packing'
    APPOINTMENT_REASON_OTHER = 'other'

    reason_list = (
        (APPOINTMENT_REASON_INSPECTION, 'Inspection'),
        (APPOINTMENT_REASON_BASICTUNEUP, 'Basic Tuneup'),
        (APPOINTMENT_REASON_ADVANCEDTUNEUP, 'Advanced Tuneup'),
        (APPOINTMENT_REASON_FLATFIX, 'Flat Fix'),
        (APPOINTMENT_REASON_ASSEMBLY, 'Bike Assembly'),
        (APPOINTMENT_REASON_BIKEPACK, 'Bike Packing'),
        (APPOINTMENT_REASON_OTHER, 'Other'),
    )