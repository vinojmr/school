const countryStateInfo = {
    Engineering: {
        Mechanical: null,
        civil: null
    },
    Medical: {
        MBBS: null,
        BDS: null
    },
    Arts: {
        BA: null,
        MA: null
    },
    Commerce: {
        Bcom: null,
        BBA : null}
};

window.onload = function() {
    const selectCountry = document.getElementById('country');
    const selectState = document.getElementById('state');

    selectState.disabled = true;

    for (let country in countryStateInfo) {
        selectCountry.options[selectCountry.options.length] = new Option(country, country);
    }

    // country change
    selectCountry.onchange = (e) => {
        selectState.disabled = false;
        selectState.length = 1; // Remove all existing state options

        for (let state in countryStateInfo[e.target.value]) {
            selectState.options[selectState.options.length] = new Option(state, state);
        }
    };
};
