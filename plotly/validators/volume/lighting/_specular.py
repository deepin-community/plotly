import _plotly_utils.basevalidators


class SpecularValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="specular", parent_name="volume.lighting", **kwargs):
        super(SpecularValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 2),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
