/* the public and secret keys are passed in from checkout.html via django  json_script template filter */
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

/* Stripe is an object from <script src="https://js.stripe.com/v3/"></script>
   So, we create a client using the API's public key */
var stripe = Stripe(stripePublicKey);

/* instantiate a stripe element */
var elements = stripe.elements();

/* below style copied from  */
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {style: style});

/* mount the 'card' element (with style) to the #card-element in checkout.html */
card.mount('#card-element');