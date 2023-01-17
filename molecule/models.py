from django.db import models


# Create your models here.


class Molecule(models.Model):
    class EsolClassOpts(models.IntegerChoices):

        soluble = 0
        moderately_soluble = 1
        very_soluble = 2
        poorly_soluble = 3
        highly_soluble = 4

    class AliClassOpts(models.IntegerChoices):
        soluble = 0
        moderately_soluble = 1
        very_soluble = 2
        poorly_soluble = 3
        highly_soluble = 4
        insoluble = 5

    class SilicosItClassOpts(models.IntegerChoices):
        soluble = 0
        moderately_soluble = 1
        poorly_soluble = 2
        insoluble = 3

    class GiAbsorptionOpts(models.IntegerChoices):
        low = 0
        medium = 1
        high = 2

    canonical_smiles = models.CharField(max_length=500)
    formula = models.CharField(max_length=100)
    mw = models.FloatField()
    heavy_atoms = models.IntegerField(verbose_name="num_heavy_atoms", default=0)
    aromatic_heavy_atoms = models.IntegerField(
        verbose_name="num_aromatic_heavy_atoms", default=0
    )
    fraction_csp3 = models.FloatField()
    rotatable_bonds = models.IntegerField(verbose_name="num_rotatable_bonds", default=0)
    hbond_acceptors = models.IntegerField(verbose_name="num_hbond_acceptors", default=0)
    hbond_donors = models.IntegerField(verbose_name="num_hbond_donors", default=0)
    mr = models.FloatField()
    tpsa = models.FloatField()
    ilogp = models.FloatField()
    xlogp3 = models.FloatField()
    wlogp = models.FloatField()
    mlogp = models.FloatField()
    silicosit_log_p = models.FloatField()
    consensus_log_p = models.FloatField()
    esol_log_s = models.FloatField()
    esol_solubility_mgml = models.FloatField()
    esol_solubility_moll = models.FloatField()
    esol_class = models.IntegerField(choices=EsolClassOpts.choices)
    ali_log_s = models.FloatField()
    ali_solubility_mgml = models.FloatField()
    ali_solubility_moll = models.FloatField()
    ali_class = models.IntegerField(choices=AliClassOpts.choices)
    silicosit_logsw = models.FloatField()
    silicosit_solubility_mgml = models.FloatField()
    silicosit_solubility_moll = models.FloatField()
    silicosit_class = models.IntegerField(choices=SilicosItClassOpts.choices)
    gi_absorption = models.IntegerField(choices=GiAbsorptionOpts.choices)
    bbb_permeant = models.BooleanField()
    pgp_substrate = models.BooleanField()
    cyp1a2_inhibitor = models.BooleanField()
    cyp2c19_inhibitor = models.BooleanField()
    cyp2c9_inhibitor = models.BooleanField()
    cyp2d6_inhibitor = models.BooleanField()
    cyp3a4_inhibitor = models.BooleanField()
    log_kp_cms = models.FloatField()
    lipinski_violations = models.IntegerField()
    ghose_violations = models.IntegerField()
    veber_violations = models.IntegerField()
    egan_violations = models.IntegerField()
    muegge_violations = models.IntegerField()
    bioavailability_score = models.FloatField()
    pains_alert = models.IntegerField()
    brenk_alerts = models.IntegerField()
    leadlikeness_violations = models.IntegerField()
    synthetic_accessibility = models.FloatField()
