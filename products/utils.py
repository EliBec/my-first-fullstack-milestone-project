class Preference:

    PRODUCT_STYLE_KID = 'kid'
    PRODUCT_STYLE_MAN = 'man'
    PRODUCT_STYLE_WOMAN = 'woman'
    PRODUCT_STYLE_UNISEX = 'unisex'

    style_choices = (
        (PRODUCT_STYLE_KID, 'Kid'),
        (PRODUCT_STYLE_MAN, 'Man'),
        (PRODUCT_STYLE_WOMAN, 'Woman'),
        (PRODUCT_STYLE_UNISEX, 'Unisex'),
    )

    RECOMMENDATION_YES = 'yes'
    RECOMMENDATION_NO = 'no'

    recommendation_choices = (
        (RECOMMENDATION_YES, 'Yes'),
        (RECOMMENDATION_NO, 'No'),
    )