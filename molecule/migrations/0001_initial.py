# Generated by Django 3.2 on 2023-01-17 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Molecule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canonical_smiles', models.CharField(max_length=500)),
                ('formula', models.CharField(max_length=100)),
                ('mw', models.FloatField()),
                ('heavy_atoms', models.IntegerField(default=0, verbose_name='num_heavy_atoms')),
                ('aromatic_heavy_atoms', models.IntegerField(default=0, verbose_name='num_aromatic_heavy_atoms')),
                ('fraction_csp3', models.FloatField()),
                ('rotatable_bonds', models.IntegerField(default=0, verbose_name='num_rotatable_bonds')),
                ('hbond_acceptors', models.IntegerField(default=0, verbose_name='num_hbond_acceptors')),
                ('hbond_donors', models.IntegerField(default=0, verbose_name='num_hbond_donors')),
                ('mr', models.FloatField()),
                ('tpsa', models.FloatField()),
                ('ilogp', models.FloatField()),
                ('xlogp3', models.FloatField()),
                ('wlogp', models.FloatField()),
                ('mlogp', models.FloatField()),
                ('silicosit_log_p', models.FloatField()),
                ('consensus_log_p', models.FloatField()),
                ('esol_log_s', models.FloatField()),
                ('esol_solubility_mgml', models.FloatField()),
                ('esol_solubility_moll', models.FloatField()),
                ('esol_class', models.IntegerField(choices=[(0, 'Soluble'), (1, 'Moderately Soluble'), (2, 'Very Soluble'), (3, 'Poorly Soluble'), (4, 'Highly Soluble')])),
                ('ali_log_s', models.FloatField()),
                ('ali_solubility_mgml', models.FloatField()),
                ('ali_solubility_moll', models.FloatField()),
                ('ali_class', models.IntegerField(choices=[(0, 'Soluble'), (1, 'Moderately Soluble'), (2, 'Very Soluble'), (3, 'Poorly Soluble'), (4, 'Highly Soluble'), (5, 'Insoluble')])),
                ('silicosit_logsw', models.FloatField()),
                ('silicosit_solubility_mgml', models.FloatField()),
                ('silicosit_solubility_moll', models.FloatField()),
                ('silicosit_class', models.IntegerField(choices=[(0, 'Soluble'), (1, 'Moderately Soluble'), (2, 'Poorly Soluble'), (3, 'Insoluble')])),
                ('gi_absorption', models.IntegerField(choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')])),
                ('bbb_permeant', models.BooleanField()),
                ('pgp_substrate', models.BooleanField()),
                ('cyp1a2_inhibitor', models.BooleanField()),
                ('cyp2c19_inhibitor', models.BooleanField()),
                ('cyp2c9_inhibitor', models.BooleanField()),
                ('cyp2d6_inhibitor', models.BooleanField()),
                ('cyp3a4_inhibitor', models.BooleanField()),
                ('log_kp_cms', models.FloatField()),
                ('lipinski_violations', models.IntegerField()),
                ('ghose_violations', models.IntegerField()),
                ('veber_violations', models.IntegerField()),
                ('egan_violations', models.IntegerField()),
                ('muegge_violations', models.IntegerField()),
                ('bioavailability_score', models.FloatField()),
                ('pains_alert', models.IntegerField()),
                ('brenk_alerts', models.IntegerField()),
                ('leadlikeness_violations', models.IntegerField()),
                ('synthetic_accessibility', models.FloatField()),
            ],
        ),
    ]
