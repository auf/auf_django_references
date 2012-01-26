$(function() {

    function etablissement_autocomplete(request, response) {
        var form = $(this.form);
        var pays = form.data('etablissement.critere_pays');
        if (pays) {
            request.pays = $(pays).val();
        }
        $.getJSON('/references/autocomplete/etablissements.json', request, response);
    }

    function etablissement_select(event, ui) {
        var form = $(this.form);
        form.find('[name=ref]').val(ui.item.id);
        ref_changed(form);
    }

    function etablissement_change(event, ui) {
        var form = $(this.form);
        if (form.data('etablissement.nom_ref') != $(this).val()) {
            form.find('[name=ref]').val('');
            ref_changed(form);
        }
    }

    function pays_change(event) {
        var form = $(this.form);
        var ref = form.find('[name=ref]');
        if (ref.val()) {
            ref.val('');
            form.find('[name=nom]').val('');
            ref_changed(form);
        }
    }

    function ref_changed(form) {
        var id = form.find('[name=ref]').val();
        if (id) {
            var critere_pays = form.data('etablissement.critere_pays');
            $.get('/references/etablissements/' + id + '.json', function(data) {
                var disabled_fields = [];
                for (field in data) {
                    if (field == 'id' || (critere_pays && field == 'pays')) {
                        continue;
                    }
                    if (field == 'nom') {
                        form.data('etablissement.nom_ref', data[field]);
                    }
                    else {
                        var widget = form.find('[name=' + field + ']');
                        if (widget.is(':checkbox')) {
                            widget.attr('checked', data[field]);
                        }
                        else {
                            widget.val(data[field]);
                        }
                        widget.attr('disabled', true);
                        disabled_fields.push(field);
                    }
                }
                form.data('etablissement.disabled_fields', disabled_fields);
            });
        }
        else {
            $.each(form.data('etablissement.disabled_fields'), function() {
                form.find('[name=' + this + ']').attr('disabled', false);
            });
            form.data('etablissement.nom_ref', '');
        }
    }

    $('input.etablissement-autocomplete').each(function() {
        var form = $(this.form);

        // Cacher le champ ref et son label
        var ref_field = form.find('[name=ref]');
        ref_field.hide();
        var ref_field_id = ref_field.attr('id');
        if (ref_field_id) {
            form.find('label[for=' + ref_field_id + ']').hide();
        }

        // On vérifie si le champ pays se trouve avant le champ à auto-compléter.
        // Si c'est le cas, on va filtrer l'auto-complétion avec le pays
        // sélectionné.
        var all_inputs = form.find(':input');
        var pays_input = all_inputs.filter('[name=pays]');
        var pays_index = all_inputs.index(pays_input);
        var my_index = all_inputs.index(this);
        if (pays_index != -1 && pays_index < my_index) {
            form.data('etablissement.critere_pays', pays_input.get());
            pays_input.change(pays_change);
        }
        else {
            form.data('etablissement.critere_pays', false);
        }

        // Réactiver les champs désactivés juste avant la soumission
        form.data('etablissement.disabled_fields', []);
        form.on('submit.etablissement', function() {
            $.each($(this).data('etablissement.disabled_fields'), function() {
                form.find('[name=' + this + ']').attr('disabled', false);
            });
        });

        // Pré-remplir les champs si une référence est déjà indiquée
        ref_changed(form);

        // Mettre en place l'autocomplete
        $(this).autocomplete({
            source: etablissement_autocomplete,
            select: etablissement_select
        });
        $(this).change(etablissement_change);
    });

});
