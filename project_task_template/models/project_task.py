# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ProjectTask(models.Model):
    _inherit = "project.task"

    task_template_id = fields.Many2one(
        string="Template",
        comodel_name="project.task_template",
        domain="[('project_template_id','=',project_template_id),('id','!=',id)]"
    )

    @api.multi
    def _prepare_post_task_data(self):
        self.ensure_one()
        return {
        }
