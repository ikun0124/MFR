"""Loss function for the MFR Model Implementation."""

# Copyright (C) 2022 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import torch
from torch import Tensor, nn


class GeneratorLoss(nn.Module):
    """Generator loss for the MFR model.
    """

    def __init__(self, wadv=1, wrec=50, wlat=1):
        super().__init__()

        self.loss_lat = nn.SmoothL1Loss()
        self.loss_adv = nn.MSELoss()
        self.loss_rec = nn.L1Loss()

        self.wadv = wadv
        self.wrec = wrec
        self.wlat = wlat

    def forward(
        self, latent_i: Tensor, latent_o: Tensor, images: Tensor, fake: Tensor, pred_real: Tensor, pred_fake: Tensor
    ) -> Tensor:
        """Compute the loss for a batch.
        """
        error_lat = self.loss_lat(latent_i, latent_o)
        error_rec = self.loss_rec(images, fake)
        error_adv = self.loss_adv(pred_real, pred_fake)

        loss = error_adv * self.wadv + error_rec * self.wrec + error_lat * self.wlat
        return loss


class DiscriminatorLoss(nn.Module):
    """Discriminator loss for the MFR model."""

    def __init__(self):
        super().__init__()

        self.loss_bce = nn.BCELoss()

    def forward(self, pred_real, pred_fake):
        """Compute the loss for a predicted batch.

        """
        error_discriminator_real = self.loss_bce(
            pred_real, torch.ones(size=pred_real.shape, dtype=torch.float32, device=pred_real.device)
        )
        error_discriminator_fake = self.loss_bce(
            pred_fake, torch.zeros(size=pred_fake.shape, dtype=torch.float32, device=pred_fake.device)
        )
        loss_discriminator = (error_discriminator_fake + error_discriminator_real) * 0.5
        return loss_discriminator
